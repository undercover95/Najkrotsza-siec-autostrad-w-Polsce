# KOMPILACJA [make]
make: GeneratorMiast.java
	javac GeneratorMiast.java

# CZYSZCZENIE [make clean]
clean:
	rm -f *.o *.x *.x~ *.c~ *~ *.class

# URUCHAMIANIE [make run]
runGen:
	java GeneratorMiast ${ARGS}
	
runGenAll:
	java GeneratorMiast 1
	java GeneratorMiast 2
	java GeneratorMiast 3
	java GeneratorMiast 4
	java GeneratorMiast 5
	java GeneratorMiast 6
	java GeneratorMiast 7
	java GeneratorMiast 8
	java GeneratorMiast 9
	java GeneratorMiast 10
	java GeneratorMiast 20
	java GeneratorMiast 30
	java GeneratorMiast 40
	java GeneratorMiast 50