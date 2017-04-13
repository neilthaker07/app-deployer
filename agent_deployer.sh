git_url="$1"
echo $git_url

git clone $git_url

SUBSTRING1=$(echo $git_url| cut -d'/' -f 5)

repo_name=$(echo $SUBSTRING1| cut -d'.' -f 1)

cd $repo_name

while read install_value; do
	pip install $install_value
done <requirements.txt

nohup python app.py