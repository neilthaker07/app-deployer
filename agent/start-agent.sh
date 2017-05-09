while read install_value; do
	pip install $install_value
done <agent-requirements.txt


nohup python agent-listener.py > agent.log 2>&1 &
