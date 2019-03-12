cd /root/luoleicn.github.io &&\
git pull &&\
jekyll build &&\
rm /var/www/html/* -rf &&\
cp -r _site/* /var/www/html/ &&\
rm -rf _site



