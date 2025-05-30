[<Sealed; AllowNullLiteral>]
type TreeNode(left: TreeNode, right: TreeNode) =
    member this.itemCheck() = 
        if isNull left then 1 else 1 + left.itemCheck() + right.itemCheck()


let rec bottomUpTree(depth: int) : TreeNode =
    if depth = 0 then //modified code: added additional check for if depth is 0
        TreeNode(null, null)
    else if depth > 0 then
        TreeNode(bottomUpTree(depth - 1), bottomUpTree(depth - 1))
    else
        TreeNode(null, null)

[<EntryPoint>]
let main args =
    let n = 10
    let minDepth = 4
    let maxDepth = max (minDepth + 2) n
    let stretchDepth = maxDepth + 1

    printfn "stretch tree of depth %d\t check: %d" stretchDepth (bottomUpTree(stretchDepth).itemCheck())

    let getDepth(depth: int) =
        depth

    let longLivedTree = bottomUpTree maxDepth
    let mutable i = 4 //variable that would have been used in the while loop is defined here as compensation for the while loop not functioning

    [| for depth in minDepth..2..getDepth(maxDepth) do //modified code: added loop invariance - f# wouldn't let this be turned into a while loop
         yield async {
            let iterations = 1 <<< (maxDepth - depth + minDepth)
            let check = Array.init iterations (fun _ -> bottomUpTree(depth).itemCheck()) |> Array.sum
            return sprintf "%d\t trees of depth %d\t check: %d" iterations depth check
         } |]
    |> Async.Parallel
    |> Async.RunSynchronously
    |> Array.iter (printfn "%s")

    printfn "long lived tree of depth %d\t check: %d" maxDepth (longLivedTree.itemCheck())
    0