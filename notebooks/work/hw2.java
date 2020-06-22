// Java implementation to construct 
// Binary Tree in level order fashion 

class Node { 
	
	int data; 
	int rcount; 
	int lcount; 
	
		Node left; 
	Node right; 
	Node(int data) 
	{ 
		this.data = data; 
		this.rcount = this.lcount = 0; 
		this.left = this.right = null; 
	} 
	
	// Function for inorder Traversal of tree. 
	static void inorder(Node root) 
	{ 
		if (root != null) { 
			inorder(root.left); 
			System.out.print(root.data + " "); 
			inorder(root.right); 
		} 
	} 
	
	// Function to check whether the given 
	// Binary tree is a perfect binary tree 
	// using the no. of nodes in tree. 
	static boolean isPBT(int count) 
	{ 
		count = count + 1; 
		
		// Loop to check the count is in 
		// the form of 2^(n-1) 
		while (count % 2 == 0) 
			count = count / 2; 
		if (count == 1) 
			return true; 
		else
			return false; 
	} 
	
	// Recursive function to insert 
	// elements in a binary tree 
	static Node insert(Node root, int data) 
	{ 
		
		// Condition when root is NULL 
		if (root == null) { 
			Node n = new Node(data); 
			return n; 
		} 
		
		// Condition when count of left sub-tree 
		// nodes is equal to the count 
		// of right sub-tree nodes 
		if (root.rcount == root.lcount) { 
			root.left = insert(root.left, data); 
			root.lcount += 1; 
		} 
		
		// Condition when count of left sub-tree 
		// nodes is greater than 
		// the right sub-tree nodes 
		else if (root.rcount < root.lcount) { 
			
			// Condition when left Sub-tree is 
			// Perfect Binary Tree then Insert 
			// in right sub-tree. 
			if (isPBT(root.lcount)) { 
				root.right = insert(root.right, data); 
				root.rcount += 1; 
			} 
			
			// If Left Sub-tree is not Perfect 
			// Binary Tree then Insert in left sub-tree 
			else { 
				root.left = insert(root.left, data); 
				root.lcount += 1; 
			} 
		} 
		return root; 
	} 
	
		// Driver Code 
	public static void main(String args[]) 
	{ 
		int arr[] = {15, 10, 20, 8, 12, 16, 25}; //{ 8, 6, 7, 12, 5, 1, 9 }; 
		int size = 7; 
		Node root = null; 
		
		// Loop to insert nodes in 
		// Binary Tree in level order Traversal 
		for (int i = 0; i < size; i++) 
			root = insert(root, arr[i]); 
		//inorder(root);
        System.out.println(root.data + " " + root.left.data + " " + root.right.data);
	} 
} 