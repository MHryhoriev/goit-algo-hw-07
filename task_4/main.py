class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.deleted = False
        self.replies = [] 
        self.height = 1
        self.parent = None

    def add_reply(self, reply):

        reply.parent = self
        self.replies.append(reply)
        self.height = 1 + max(self.get_height(reply) for reply in self.replies)
        self.balance_tree()

    def remove_reply(self):
        """
        Marks this comment as deleted and sets its text to a default message.
        """
        self.deleted = True

        if self.parent:
            self.parent.balance_tree()

    def display(self, indent=0):
        """
        Recursively displays the comment and its replies with indentation for hierarchy.
        """
        result = '    ' * indent
        if self.deleted:
            result += 'Цей коментар було видалено.'
        else:
            result += f'{self.author}: {self.text}'

        print(result)

        for reply in self.replies:
            reply.display(indent + 1)

    def get_height(self, node):
        """
        Returns the height of the node.
        """
        return node.height if node else 0

    def get_balance(self):
        """
        Returns the balance factor of the comment.
        """
        left_height = self.get_height(self.replies[0]) if len(self.replies) > 0 else 0
        right_height = self.get_height(self.replies[1]) if len(self.replies) > 1 else 0
        return left_height - right_height

    def left_rotate(self):
        """
        Performs a left rotation on the comment.
        """
        new_root = self.replies[1]
        self.replies[1] = new_root.replies[0]
        new_root.replies[0] = self
        self.height = 1 + max(self.get_height(self.replies[0]), self.get_height(self.replies[1]))
        new_root.height = 1 + max(self.get_height(new_root.replies[0]), self.get_height(new_root.replies[1]))
        return new_root

    def right_rotate(self):
        """
        Performs a right rotation on the comment.
        """
        new_root = self.replies[0]
        self.replies[0] = new_root.replies[1]
        new_root.replies[1] = self
        self.height = 1 + max(self.get_height(self.replies[0]), self.get_height(self.replies[1]))
        new_root.height = 1 + max(self.get_height(new_root.replies[0]), self.get_height(new_root.replies[1]))
        return new_root

    def balance_tree(self):
        """
        Balances the comment tree if necessary.
        """
        balance = self.get_balance()
        
        if balance > 1:
            if self.get_balance() < 0:
                self.replies[0] = self.replies[0].right_rotate()
            return self.left_rotate()

        if balance < -1:
            if self.get_balance() > 0:
                self.replies[1] = self.replies[1].left_rotate()
            return self.right_rotate()
        
        return self

def main():
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()

if __name__ == "__main__":
    main()