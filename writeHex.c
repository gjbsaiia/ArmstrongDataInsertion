#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

void writeData(char * buff, const char* path){
	char sep[2] = "_";
	char* token;
	float f;
	uint32_t conv;
	FILE * file = fopen( path, "w+");
	token = strtok(buff, sep);
	int i = 0;
	int bitCount = 0;
	while(token != NULL){
		f = floorf(atof(token) * 100) / 100;   // to two decimals
		conv = *(uint32_t *)&f;
		bitCount += sizeof(conv);
		fprintf(file, "%d ", conv);
		token = strtok(NULL, sep);
		i += 1;
	}
	fprintf(stdout, "%d data points, %d bits\n", i, bitCount);
	fclose(file);
}

int read_write_Data(const char* path){
	FILE * file = fopen( path, "r" );
	char* buff = (char *)malloc(37000 * sizeof(char));
	fscanf(file, "%s", buff);
	writeData(buff, path);
	free(buff);
	buff = NULL;
	return 1;
}

int main(int argc, char **argv){
	const char * path = "/samba/mountedFolder/test.txt";
	int status = read_write_Data(path);
	if(status){
		printf("float data converted to int representations.\n");
	}
	else{
		printf("process failed\n");
	}
}
