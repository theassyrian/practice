#ifndef PRACTICE_STACK_STACK_H
#define PRACTICE_STACK_STACK_H

#include "list.h"

typedef List Stack;

#define stack_init list_init
#define stack_destroy list_destroy

Stack *stack_create();
void stack_push(Stack *stack, const int data);
int stack_pop(Stack *stack);
int stack_top(Stack *stack);

#endif
