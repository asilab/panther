.PHONY: all clean

CXX = g++ -std=c++14
CXXFLAGS = -Wall -Wextra -O3 -m64 -g -I./include
LFLAGS = -pthread

objects = PGMRead.o \
		  PGMWrite.o \
		  divide.o \
		  main.o

objects2 = PGMRead.o \
		  hdc.o \
		  alpha.o \
		  main2.o

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

div: $(objects)
	$(CXX) $(LFLAGS) $^ -o $@

hdc: $(objects2)
	$(CXX) $(LFLAGS) $^ -o $@

all: div \
	 hdc


clean:
	rm -f *.o div hdc

# Dependencies

PGMRead.o: PGMRead.h PGMRead.cpp

PGMWrite.o: PGMWrite.cpp PGMWrite.h

hdc.o: hdc.cpp hdc.h

alpha.o: alpha.cpp alpha.h

divide.o: divide.cpp divide.h

main.o: main.cpp PGMRead.h PGMWrite.h divide.h

main2.o: main2.cpp PGMRead.h hdc.h alpha.h