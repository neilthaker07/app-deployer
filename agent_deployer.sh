git_url="$1"
echo $git_url

SUBSTRING1=$(echo $git_url| cut -d'/' -f 5)

repo_name=$(echo $SUBSTRING1| cut -d'.' -f 1)

for folder in */ ; do
    echo "$folder"
done

foldername=$(echo $folder| cut -d'/' -f 1)

if [ "$foldername" == "$repo_name" ]; then
	cd $repo_name 
	git pull
else
	git clone $git_url
	cd $repo_name
fi

while read install_value; do
	pip install $install_value
done <requirements.txt

nohup python app.py