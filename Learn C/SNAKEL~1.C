#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//#include <conio.h>

int ladderMove(int a);
int snakeMove(int a);


int main(){
	int playerPos=0, botPos=0;      // start position for all player is 0
	int rollValue1, rollValue2;
//	int counter=0;
	char die;
//	 clrscr();

	do{
		srand(time(NULL));         // seed the random function
//		counter++;

/*
		if(counter>10){
			counter = 0;
			clrscr();
		}
*/

		if(playerPos >= 100){
			printf("You won\n");
			break;
		}
		else if(botPos >= 100){
			printf("You lost\n");
			break;
		}

		printf("1. Enter 0 to Exit\n2. Enter any value other than 0 to Continue\n");
		die = getchar();
		printf("\n");

		rollValue1 = (rand()%6)+1;
		printf("You rolled %2d \t", rollValue1);
		if(playerPos == 0 && (rollValue1 == 1 || rollValue1 == 6)){  // start condition
			playerPos = 1;
			printf("You moved to %d \n",1);
		}
		else if(playerPos != 0){                                  // moving condition
			if(playerPos>94 && rollValue1==100-playerPos){          // if pos is 94 above then move for pos to 100
				playerPos += rollValue1;
				playerPos = ladderMove(playerPos);
				playerPos = snakeMove(playerPos);
			}
			else if (playerPos>94 && rollValue1<=100-playerPos)     // if pos is 94 above and roll value is less than diff of pos and 100
			{
				playerPos += rollValue1;
				playerPos = ladderMove(playerPos);
				playerPos = snakeMove(playerPos);
			}
			else if (playerPos<94)
			{
				playerPos += rollValue1;
				playerPos = ladderMove(playerPos);
				playerPos = snakeMove(playerPos);
			}
			else{
				printf("You cannot moved because rolled value is greater than steps left");
			}
			if(playerPos >= 100){
				printf("Player moved to %3d\n",100);
			}
			else{
				printf("Player moved to %3d\n", playerPos);
			}
		}
		else{
			printf("You were at start and did not roll a 1 or 6\n");
		}


		rollValue2 = (rand()%6)+1;
		printf("Bot rolled %2d \t", rollValue2);
		if(botPos == 0 && (rollValue2 == 1 || rollValue2 == 6)){
			botPos = 1;
			printf("Bot moved to %3d \n",1);
		}
		else if(botPos != 0){
			if(botPos>94 && rollValue2==100-botPos){
				botPos += rollValue2;
				botPos = ladderMove(botPos);
				botPos = snakeMove(botPos);
			}
			else if (botPos>=94 && rollValue1<=100-botPos)
			{
				botPos += rollValue2;
				botPos = ladderMove(botPos);
				botPos = snakeMove(botPos);
			}
			else if (botPos<94)
			{
				botPos += rollValue2;
				botPos = ladderMove(botPos);
				botPos = snakeMove(botPos);
			}
			else{
				printf("Bot cannot moved because rolled value is greater than steps left");
			}
			if(botPos >= 100){
				printf("Bot moved to %3d\n",100);
			}
			else{
				printf("bot moved to %3d\n", botPos);
			}
		}
		else{
			printf("Bot was at start and did not roll a 1 or 6\n");
		}
		printf("\n");

	}while(die!='0');
	printf("Exit");
//	getch();
	return 0;
}


int ladderMove(int a){   // Used to move the position if player reaches a ladder
	if(a == 4){
		return 14;
	}
	else if(a == 9){
		return 31;
	}
	else if(a == 28){
		return 84;
	}
	else if(a == 21){
		return 31;
	}
	else if(a == 67){
		return 72;
	}
	else if(a == 80){
		return 95;
	}
	else{
		return a;
	}
}

int snakeMove(int a){   // Used to move the position if player reaches a snake
	if(a == 17){
		return 7;
	}
	else if(a == 54){
		return 34;
	}
	else if(a == 33){
		return 2;
	}
	else if(a == 63){
		return 13;
	}
	else if(a == 87){
		return 36;
	}
	else if(a == 93){
		return 73;
	}
	else if(a == 94){
		return 75;
	}
	else if(a == 98){
		return 18;
	}
	else{
		return a;
	}
}