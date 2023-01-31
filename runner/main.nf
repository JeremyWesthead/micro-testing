nextflow.enable.dsl=2

process getFiles {
    input:
        val batch
    output:
        path "${batch}", emit: p
    script:
        """
        mkdir ${batch}
        #Checking for hostnames vs localhost
        curl db:8003 && DB="db" || DB="127.0.0.1"
        curl input-manager:8001 && INPUTMANAGER="input-manager" || INPUTMANAGER="127.0.0.1"
        for sample in \$(curl -s \$DB:8003/batch?guid=${batch} | jq -r ".samples[]")
            do
                echo \$(curl -s \$INPUTMANAGER:8001/fetch?guid=\$sample | jq -r  ".file") > ${batch}/\$sample.fastq
            done
        """
}

process doSomething {
    input:
        val batch
    script:
        """
        touch ${batch}/outFile.txt
        #Checking for hostnames vs localhost
        curl db:8003 && DB="db" || DB="127.0.0.1"
        curl output-manager:8002 && OUTPUTMANAGER="output-manager" || OUTPUTMANAGER="127.0.0.1"
        for sample in \$(curl -s \$DB:8003/batch?guid=\$(basename ${batch}) | jq -r ".samples[]")
            do
                cat ${batch}/\$sample.fastq >> ${batch}/outFile.txt
            done
        #Upload this output file
        curl -X POST \
            "\$OUTPUTMANAGER:8002/put?guid=\$(basename ${batch})&files=%7B%22outFile.txt%22%3A%20%22\$(base64 -w 0 ${batch}/outFile.txt)%22%7D" \
            -H 'accept: application/json' \
            -d ''
        """
}

workflow {
    main:
        getFiles(params.guid)
        doSomething(getFiles.out.p)
}
