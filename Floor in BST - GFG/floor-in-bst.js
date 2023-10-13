//{ Driver Code Starts
//Initial Template for javascript

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

class Node {
    constructor(data) {
        this.data = data;
        this.right = null;
        this.left = null;
    }
}



function insert(tree, val) {
    if (tree === null) return new Node(val);
    
    if (val < tree.data) {
        tree.left = insert(tree.left, val);
    } else if (val > tree.data) {
        tree.right = insert(tree.right, val);
    }

    return tree;
}

function main() {
    const t = parseInt(readLine());
    for(let i = 0; i < t; i++) {
        let root = null;

        const n = parseInt(readLine());
        const elements = readLine().split(' ').map(Number);

        for (const el of elements) {
            root = insert(root, el);
        }

        const s = parseInt(readLine());
        
        console.log(floor(root, s));
    }
}



// } Driver Code Ends
//User function Template for javascript
function floor(root, x) {
    //code here
    var value = -1;
    var node = root;
    
    while (node != null){
        if (node.data == x){
            return x;
        }
        else if (node.data < x){
            value = Math.max(value, node.data);
            node = node.right;
        } else if (node.data > x){
            node = node.left;
        }
    }
    return value;
}

//{ Driver Code Starts.
// } Driver Code Ends