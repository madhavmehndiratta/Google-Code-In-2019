CC = g++
CFLAGS = -Wall -g
CPPTARGET = createData

py = python3
target = plot

all: generate plot

generate: $(CPPTARGET).cpp
	$(CC) $(CFLAGS) -o $(CPPTARGET) $(CPPTARGET).cpp
	chmod +x $(CPPTARGET)
	./$(CPPTARGET)
	@echo Welcome to the Introduction to Makefile!
	@echo
	@echo This file will generate some random data and plot it on a graph.
	@echo
	@echo Data Generation Successfull!
	@echo

plot: $(target).py
	@echo Plotting the Graph....
	@echo
	$(py) $(target).py

clean:
	rm -rf $(CPPTARGET) data.txt
