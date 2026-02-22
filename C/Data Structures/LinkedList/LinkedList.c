#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct LinkedList
{
    char *s;
    struct LinkedList *next;
} Linked;


void putstr(char *s)
{
    int i = 0;
    if (!s)
        return ;
    while (s[i])
    {
        write(1, &s[i], 1);
        i++;
    }
    write(1, "\n", 1);

}


Linked * create_Node(char *s)
{
    Linked *node = malloc(sizeof(Linked));
    if (!node)
        return 0x0;

    node->s = malloc(strlen(s) + 1);
    if (!node->s)
        return 0x0;

    strcpy(node->s, s);
    node->next = NULL;

    return node ;
}

void add_at_beginning(Linked **head, char *s)
{

    Linked *new_Node = create_Node(s);

    new_Node->next = *head;
    *head = new_Node;
}

Linked * last_Node(Linked **head)
{
    Linked *tmp = *head;

    while (tmp->next)
    {
        tmp = tmp->next;
    }
    return (tmp);
}

int length_Node(Linked ** head)
{
    int c = 0;

    Linked * tmp = *head;
    while (tmp)
    {
        c++;
        tmp = tmp->next;
    }
    return c;
}

void add_at_end(Linked **head, char *s)
{
    Linked *new_Node = create_Node(s);
    if (!*head)
    {
        *head = new_Node;
        return ;
    }
    last_Node(head)->next = new_Node;
}

void free_list(Linked* head)
{
    Linked * tmp ;

    while (head)
    {
        tmp = head;
        head = head->next;
        free(tmp->s);
        free(tmp);
    }
}

void print_List(Linked **head)
{
    Linked * tmp = *head;

    while (tmp)
    {
        putstr(tmp->s);

            tmp = tmp->next;
        }

}

char *search_Node(Linked **head, char *s)
{
    Linked *tmp = *head;

    while (tmp)
    {
        if (!strcmp(tmp->s, s))
            return "Found";
        tmp = tmp->next;
    }
    return "Not Found";
}

char *delete_Node(Linked** head, char *s)
{
    if (!*head)
        return "Not Deleted";

    Linked *temp;

    if (!strcmp((*head)->s, s))
    {
        Linked *t = *head;
        *head = (*head)->next;
        free(t->s);
        free(t);
        return "Deleted";
    }

    temp = *head;
    while (temp->next)
    {
        if (!strcmp(temp->s, s))
        {
            Linked *i = temp->next;
            temp->next = temp->next->next;
            free(temp->s);
            free(temp);
            return "Deleted";
        }
        temp = temp->next;
    }
    return "Not Deleted";

}

int get_Index(Linked **head, Linked *node)
{
    Linked *tmp = *head;
    int c = 0;
    while (tmp)
    {
        if (tmp == node)
            return c;
        c++;
        tmp = tmp->next;
    }
    return 0;
}


Linked* find_by_Index(Linked **head, int pos)
{
    if (!*head)
        return 0x0;
    Linked *tmp = *head;

    int o = 0;
    while (tmp)
    {
        if (pos == o)
            return tmp;
        o++;
        tmp = tmp->next;
    }
    return 0x0;
}

void replace_in_Index(Linked **head, Linked *node, int pos)
{
    Linked *tmp = *head;

    int index = get_Index(head, node);
    int c = 0;
    while (tmp->next)
    {
        if (c == index)
        {
            node->next = tmp->next;
            tmp->next = node;
            return ;
        }
        c++;
        tmp = tmp->next;
    }
}

void insert_Node(Linked **head, char *s, int position)
{
    if (!*head)
        return ;
    if (length_Node(head) < position)
    {
        putstr("The Position you entred is out of the range.");
        return ;
    }

    Linked *node = find_by_Index(head, position);
    if (!node)
        putstr("Node Not Found!");

    Linked *new_Node = create_Node(s);

    replace_in_Index(head, new_Node, position);





}

int main()
{
    Linked *head = 0x0;

    add_at_end(&head, "Moukhlij");
    add_at_beginning(&head, "Younes");
    add_at_end(&head, "My NickName : Younan");

    print_List(&head);

    printf("Looking for Younes in List: %s \n", search_Node(&head, "Younes"));

    printf("--------------------------------------\n  Length of the list is : %d\n", length_Node(&head));

    printf("Deleting a node with str 'Younes' in List: %s \n", delete_Node(&head, "Younes"));
    putstr("-----------------------------------\n");
    print_List(&head);

    add_at_beginning(&head, "Younes");

    // insert node
    insert_Node(&head, "I study at 1337", 3);
    putstr("-------------------2----------------");
    print_List(&head);
    putstr("-----------------------------------");


    free_list(head);

}
