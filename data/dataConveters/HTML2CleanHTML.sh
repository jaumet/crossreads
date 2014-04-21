#!/bin/bash
OLD="xyz"
NEW="abc"
DPATH="/home/you/foo/*.txt"
BPATH="/home/you/bakup/foo"
TFILE="/tmp/out.tmp.$$"
[ ! -d $BPATH ] && mkdir -p $BPATH || :
for f in $DPATH
do
  if [ -f $f -a -r $f ]; then
    /bin/cp -f $f $BPATH
   sed "s/$OLD/$NEW/g" "$f" > $TFILE && mv $TFILE "$f"
  else
   echo "Error: Cannot read $f"
  fi
done
/bin/rm $TFILE

####################################################
# 
#      > List of replacements:
#        <HTML>*.<BODY> -> ''
#        <P(*.=> -> <P>
#        <DIV*.> -> ''
#        </DIV> -> <> ''
#        </BODY>*.</HTML> -> '' 
#        <FONT*.> -> ''
#        </FONT> -> ''
#        <BR> -> <> ''
#        <I> -> <i>
#        <B> -> <b>
#        </I> -> </i>
#        </B> -> </b>
#        <(*.)> -> <>
#        <(*.)> -> <>

#        <P>[only bspc]</P> -> ''

#      > Add options to convert also special characters
#        á -> &aacute;
#        é -> &eacute;
#        í -> &iacute;
#        ó -> &oacute;
#        ú -> &uacute;
#        à -> &agrave;
#        è -> &egrave;
#        ò -> &ograve;
#        Á -> &Aacute;
#        É -> &Eacute;
#        Í -> &Iacute;
#        Ó -> &Oacute;
#        Ú -> &Uacute;
#        À -> &Agrave;
#        È -> &Egrave;
#        Ò -> &Ograve;
#         -> &;
#         -> &;
#         -> &;
#         -> &;
#         -> &;
#         -> &;
#         -> &;
#         -> &;
#         -> &;
