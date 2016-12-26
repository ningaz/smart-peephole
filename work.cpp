#include <unistd.h>
#include <signal.h>
#include <stdlib.h>

#include <string>

#include "mraa/gpio.h"

bool shouldRun = true;
int cnt = 0;
int oldCnt = 0;

//Ctrl-C handler
void sig_handler(int signo) {
    if (signo == SIGINT)
        shouldRun = false;
}

//interrupt handler
void interrupt(void* args) {
	cnt++;
	//using bash from programm
	int status = system("./screenshot.sh 2> /dev/null");
	if(!status) {
		status = system("python slack.py 2> /dev/null");
	}
	
}

int main() {
	signal(SIGINT, sig_handler);

	mraa_init();
	mraa_gpio_context btn = mraa_gpio_init(2);
	mraa_gpio_context buzz = mraa_gpio_init(6);

	mraa_gpio_dir(btn, MRAA_GPIO_IN);
	mraa_gpio_dir(buzz, MRAA_GPIO_OUT);

	mraa_gpio_isr(btn, MRAA_GPIO_EDGE_FALLING, interrupt, NULL);
	
    while (shouldRun) {
	usleep(50000);
	//if value is changing, Buzzer is making a sound
	if(cnt != oldCnt) {
		mraa_gpio_write(buzz, 1);
		oldCnt = cnt;
		usleep(500000);
	} else {
		mraa_gpio_write(buzz, 0);
	}
    }	
	
    mraa_gpio_close(btn);
    mraa_gpio_close(buzz);
    return MRAA_SUCCESS;
}

