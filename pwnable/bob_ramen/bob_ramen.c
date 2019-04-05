#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <signal.h>
#include <seccomp.h>
int shin;
int zapa;
int anseong;
int neoguli;
int samyang;
int yuggae;
int jin;

int all_fat;

int init_Ramens()
{
   int ran;
   unsigned int result;
   unsigned int buf;
   int fd;

   fd = open("/dev/urandom", 0);
   if( read(fd, &buf, 4) != 4)
   {
	puts("/dev/urandom error");
	exit(0);
   }
   close(fd);
   srand(buf);

   shin = 0xDEADBEEF * rand() % 0xCAFEBABE;
   zapa = 0xDEADBEEF * rand() % 0xCAFEBABE;
   anseong = 0xDEADBEEF * rand() % 0xCAFEBABE;
   neoguli = 0xDEADBEEF * rand() % 0xCAFEBABE;
   samyang = 0xDEADBEEF * rand() % 0xCAFEBABE;
   yuggae = 0xDEADBEEF * rand() % 0xCAFEBABE;
   jin = 0xDEADBEEF * rand() % 0xCAFEBABE;
   ran = rand();
   result = jin + yuggae + samyang + neoguli + anseong + zapa + shin;
   all_fat = result;
   return result;
}
void Shin()
{
   printf("You found  \"Shin Ramen \" (FAT + %d)\n", shin);
}
void Zapa()
{
   printf("You found \"Zapagetty \" (FAT + %d)\n", zapa);
}
void Anseong()
{
   printf("You found \"Anseong Tangmyeon \" (FAT + %d)\n", anseong);
}
void Neoguli()
{
   printf("You found \"Neoguli Ramen \" (FAT + %d)\n", neoguli);
}
void Samyang()
{
   printf("You found \"Samyang Ramen \" (FAT + %d)\n", samyang);
}
void Yuggaejang()
{
  printf("You found \"Yuggaejang Ramen \" (FAT + %d)\n", yuggae);
}
void Jin()
{
  printf("You found \"Jin Ramen \" (FAT + %d)\n", jin);
}

void hint()
{
	puts("There are most famous Ramen in Korea");
	puts("Find all Ramen, and Eat it!");
}

int hackme();

int main()
{
	scmp_filter_ctx ctx;
	setvbuf(stdout, 0, 2, 0);
	setvbuf(stdin, 0, 2, 0);
	alarm(0x3c);
	hint();
	init_Ramens();
	ctx = seccomp_init(0);
	seccomp_rule_add(ctx, 0x7FFF0000, 173, 0);
        seccomp_rule_add(ctx, 0x7FFF0000, 5, 0);
        seccomp_rule_add(ctx, 0x7FFF0000, 3, 0);
        seccomp_rule_add(ctx, 0x7FFF0000, 4, 0);
        seccomp_rule_add(ctx, 0x7FFF0000, 252, 0);
        seccomp_load(ctx);
	hackme();
	return 0;
}

int hackme()
{
   char str[100];
   int fd;
   int input;
    

   printf("Select Menu: ");
   scanf("%d", &input);
   getchar();
   
    if( input == shin)
      Shin();
    else if(input == zapa)
      Zapa();
    else if(input == anseong)
      Anseong();
    else if(input == neoguli)
      Neoguli();
    else if(input == samyang)
      Samyang();
    else if(input == yuggae)
      Yuggaejang();
    else if(input == jin)
      Jin();
    else
    {
      puts("How many FAT did you earned? : ");
      gets(str);
      if( atoi(str) == all_fat)
      {
	fd = open("flag", 0);
	read(fd, str, 0x64);
	puts(str);
	close(fd);
	exit(0);
      }
      puts("You'd better pull more fat to eat Ramens");
      }
    return 0;
}
