nextflow.enable.dsl=2

process getFiles {
    debug true
    input:
        val batch
    output:
        path "${batch}", emit: p
    script:
        """
        mkdir ${batch}
        for sample in \$(curl -s http://127.0.0.1:8003/batch?guid=${batch} | jq -r ".samples[]")
            do
                echo \$(curl -s http://127.0.0.1:8001/fetch?guid=\$sample | jq -r  ".file") > ${batch}/\$sample.fastq
            done
        """
}

process doSomething {
    debug true
    input:
        val batch
    script:
        """
        touch ${batch}/outFile.txt
        for sample in \$(curl -s http://127.0.0.1:8003/batch?guid=\$(basename ${batch}) | jq -r ".samples[]")
            do
                cat ${batch}/\$sample.fastq >> ${batch}/outFile.txt
            done
        #Upload this output file
        curl -X POST \
            "http://127.0.0.1:8002/put?guid=\$(basename ${batch})&files=%7B%22outFile.txt%22%3A%20%22\$(base64 -w 0 ${batch}/outFile.txt)%22%7D" \
            -H 'accept: application/json' \
            -d ''
        """
}

workflow {
    main:
        getFiles(params.guid)
        doSomething(getFiles.out.p)
}