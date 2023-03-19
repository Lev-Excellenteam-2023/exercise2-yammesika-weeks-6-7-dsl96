class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.

        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.

            >>> po_box = PostOffice(['a', 'b'])
            >>> message_id = po_box.send_message('a', 'b', 'Hello!')
            >>> len(po_box.boxes['b'])
            1
            >>> message_id
            1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user_name, num_msgs=None):
        """ Read messages by user name.

        Args:
            user_name (str): Username to receive his message.

            num_msgs (int, optional): The max number of messages the user wants to receive , default all messages.

        Returns:
            list of dict: messages.

        Raises:
            KeyError: If the user_name does not exist.
            keyError: If num_msgs less then zero

        Examples:

            >>> po_box = PostOffice(['a', 'b'])
            >>> po_box.send_message('a', 'b', 'Hello!')
            >>> po_box.read_inbox('b')
            [{'id': 1, 'body': 'Hello!', 'sender': 'a'}]

        """
        user_box = self.boxes[user_name]

        if num_msgs is None:
            num_msgs = len(user_box)

        if num_msgs < 0:
            raise ValueError(f'num_msgs must by greater then or equal to zero but found {num_msgs}')

        ret_msgs = user_box[:num_msgs]
        self.boxes[user_name] = user_box[num_msgs:]

        return ret_msgs

    def search_inbox(self, user_name, string):
        """ Read messages that contain 'string' by user name.

        Args:
            user_name (str): Username to receive his message.

            string (str):  Substring to get messages that contain it.

        Returns:
            list of dict: messages.

        Raises:
            KeyError: If the user_name does not exist.

        Examples:

          >>>po_box = PostOffice(['a', 'b'])
          >>>po_box.send_message('a', 'b', 'Hello!')
          >>>po_box.send_message('a', 'b', 'Bello!')
          >>>po_box.search_inbox('b','B')
          [{'id': 2, 'body': 'Bello!', 'sender': 'a'}]

        """
        user_box = self.boxes[user_name]

        ret_lst = []
        filter_lst = []
        for msg in user_box:
            if string in msg['body']:
                ret_lst.append(msg)
            else:
                filter_lst.append(msg)

        self.boxes[user_name] = filter_lst
        return ret_lst