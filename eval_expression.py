def add(x, y):
        return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x // y

class BinaryTree:
    # store operators to functions
    operator_funcs = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "//": divide
        }
    def __init__(self):
        self.root = None
        self.final_value = 0

    def add_expressions(self, expression, operator1, operator2):
        index = 0
        while index < len(expression) and (operator1 in expression or operator2 in expression):
            possible_operator = expression[index]
            if possible_operator == operator1 or possible_operator == operator2:
                # add the root of the expression to be added
                operation_func = operator_funcs[possible_operator]
                parent = BinaryTreeNode(operation_func)
                # add the second operand of this expression
                second_operand = int(expression[index - 1])
                second_op = BinaryTreeNode(second_operand)
                parent.right = second_op
                # find the first operand - if this is the first expression
                if self.root is None:
                    left_op_index = index - 2
                    # traverse backwards, find the first int
                    while left_op_index > 0:
                        possible_integer = expression[left_op_index]
                        # verify we have an int
                        if not possible_integer in operation_func.keys():
                            break
                        else:
                            left_op_index -= 1
                    left_operand = int(expression[left_op_index])
                    left_op = BinaryTreeNode(left_operand)
                    parent.left = left_op
                    full_expression.root = parent
                    # remove the left operand from the list
                    expression.pop(left_op_index)
                else:  # if this is not the first expression to be added
                    # make the current root the left subchild
                    parent.left = self.root
                    # promote this expression as the root
                    self.root = parent
                # remove the elements used for the expression, from the list
                expression.remove(possible_operator)
                expression.remove(second_operand)
            index += 1
        return expression
    
    def post_order_DFS(self, node=None):
        # start at the root
        if node is None:
            node = self.root
        # visit the left subtree
        if node.left is not None:
            left_side = self.post_order_DFS(node.left)
        # visit the right subtree
        if node.right is not None:
            right_side = self.post_order_DFS(node.right)
        # visit node itself - maybe an int or an operator
        if node.left is None and node.right is None:
            # this is a left, and is an int
            return node.data
        else:  # node is an operator
            operation = operator_funcs[node.data]
            return operation(left_side, right_side)
        
        

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def evaluate_expression(expression):
    # build the tree for evaluating the expression
    index = 0
    full_expression = BinaryTree()
    # add all multiplication/division first, then addition and subtraction
    expression = full_expression.add_expressions(expression, '*', '/')
    full_expression.add_expressions(expression, '+', '-')
    # calculate the final value
    return full_expression.post_order_DFS()


if __name__ == '__main__':
    expression = ["3", "4", "+", "5", "-"]
    print(evaluate_expression(expression))