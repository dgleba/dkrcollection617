#=================================================

# use this to start the script below $bse

bse=tarnosudo617;
indr=/ap/dkr/dkrcollection617a;

odr=/ap/zip;
cd $odr;


#=================================================


function tarns () {


echo $odr
echo $odr/${bse}_stdout.log

# bash tarnosudo617  2>&1 | tee -a /ap/zip/outtarnosudo.txt
# bash $indr/$bse  > >(tee  $odr/${bse}_stdout.log) 2> >(tee  $odr/${bse}_stderr.log >&2);

bash $indr/$bse  > >(tee  ${bse}_stdout.log) 2> >(tee  ${bse}_stderr.log >&2);

}


#=================================================


function   notes   () {

echo $odr
# How to redirect stderr and stdout to different files in the same line in script?
cd /ap/dkr/dkrcollection617a/bmark616h-yard/sysdata
# find .  2> error 1> output
find .  2> >(tee  error.log) 1> output.log
find .  2>&1 | tee -a $od/out_notes.txt

}

#=================================================


#
tarns

#notes
