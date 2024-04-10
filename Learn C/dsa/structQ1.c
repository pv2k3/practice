#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *next;
} link;

void create(link *);
void insertEnd(link *);
link *insertBeg(link *);
link *removeBeg(link *);
void removeEd(link *);
void show(link *);

int main()
{
    int choice;
    link *head = malloc(sizeof(link));
    create(head);
    do
    {
        printf("Enter your choice\n");
        printf("\t1. Insert at end\n\t2.Insert at beginning\n");
        printf("\t3. Remove from Beginning\n\t4.Remove fom end\n");
        printf("\t5. Show\n\t6. Exit\n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            insertEnd(head);
            break;
        case 2:
            head = insertBeg(head);
            break;
        case 3:
            head = removeBeg(head);
            break;
        case 4:
            removeEd(head);
            break;
        case 5:
            show(head);
            break;
        case 6:
            exit(0);
        default:
            printf("Wrong choice");
            break;
        }
    } while (choice != 6);
    return 0;
}
link *removeBeg(link *ptr)
{
    link *new;
    new = ptr;
    ptr = ptr->next;
    free(new);
    return ptr;
}
void create(link *ptr)
{
    printf("Enter the frist element of the linked list : ");
    scanf("%d", &ptr->data);
    ptr->next = NULL;
}
link *insertBeg(link *ptr)
{
    link *elem = malloc(sizeof(link));
    printf("Value to insert in the beginning");
    scanf("%d", &elem->data);
    elem->next = ptr;
    return elem;
}
void insertEnd(link *ptr)
{
    link *new;
    int c;
    do
    {
        new = malloc(sizeof(link));
        new->next = NULL;
        printf("Enter a element : ");
        scanf("%d", &new->data);
        printf("Enter 1 to enter another element : ");
        scanf("%d", &c);
        ptr->next = new;
        ptr = ptr->next;
    } while (c == 1);
}
void removeEd(link *ptr)
{
    link *secondLast;
    while (ptr->next != NULL)
    {
        secondLast = ptr;
        ptr = ptr->next;
    }
    secondLast->next = NULL;
    free(ptr);
}
void show(link *ptr)
{
    while (ptr->next != NULL)
    {
        printf("%d\n", ptr->data);
        ptr = ptr->next;
    }
    printf("%d\n", ptr->data);
}