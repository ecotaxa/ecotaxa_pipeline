#!/bin/bash

orginalPath=$PWD

cd tests/cytosense

sample="ecotaxa_R4_photos_flr16_2uls_10min 2022-09-14 12h28.tsv"
prefixPath="result/mock_small_data"
suffixPath="/_work"

reference="${prefixPath}_reference${suffixPath}"
totest="${prefixPath}${suffixPath}"

echo sample: ${sample}
echo reference: ${reference}/${sample}
echo to test: ${totest}/${sample}
echo 

DIFF=$(diff "${totest}/${sample}" "${reference}/${sample}")
if [ "$DIFF" != "" ] 
then
    echo "tsv is different"
else
    echo "tsv OK"
fi

lsRefTmpFile=lsref.tmp
lsToTestTmpFile=lstotest.tmp

ls -1 "${totest}" > $lsToTestTmpFile
ls -1 "${reference}" > $lsRefTmpFile

DIFF=$(diff $lsRefTmpFile $lsToTestTmpFile) 
if [ "$DIFF" != "" ] 
then
    echo "The directory is different"
else
    echo "files OK"
fi

rm -f $lsRefTmpFile $lsToTestTmpFile


cd $originalPath
