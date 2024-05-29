.PHONY: run_all

run_all: run_forwarder run_sequencer run_clients

run_forwarder:
	@echo "Running Forwarder and Router..."
	@gnome-terminal -- python3 forward.py --nc 5

run_sequencer:
	@echo "Running Sequencer..."
	@sleep 2
	@gnome-terminal -- python3 main.py --id sequencer

run_clients:
	@echo "Running Clients..."
	@sleep 2
	@gnome-terminal -- python3 main.py --id c1 --com test/test1.txt -o results
	@gnome-terminal -- python3 main.py --id c2 --com test/test2.txt -o results
	@gnome-terminal -- python3 main.py --id c3 --com test/test3.txt -o results
	@gnome-terminal -- python3 main.py --id c4 --com test/test4.txt -o results
