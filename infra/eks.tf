resource "aws_eks_node_group" "ng-igti-edc-desafiofinal" {
  cluster_name    = aws_eks_cluster.k8s-igti-edc-desafiofinal.name
  node_group_name = "ng-igti-edc-desafiofinal"
  node_role_arn   = aws_iam_role.igti-edc-desafiofinal.arn
  subnet_ids      = ["subnet-9b55fdf0", "subnet-e7450cab"]
  capacity_type = "SPOT"

  scaling_config {
    desired_size = 1
    max_size     = 1
    min_size     = 1
  }

  update_config {
    max_unavailable = 2
  }

  # Ensure that IAM Role permissions are created before and deleted after EKS Node Group handling.
  # Otherwise, EKS will not be able to properly delete EC2 Instances and Elastic Network Interfaces.
  depends_on = [
    aws_iam_role_policy_attachment.igti-edc-AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.igti-edc-AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.igti-edc-AmazonEC2ContainerRegistryReadOnly,
  ]
}

resource "aws_eks_cluster" "k8s-igti-edc-desafiofinal" {
  name     = "k8s-igti-edc-desafiofinal"
  role_arn = aws_iam_role.igti-edc-desafiofinal.arn

  vpc_config {
    subnet_ids = ["subnet-9b55fdf0", "subnet-e7450cab"]
  }


  # Ensure that IAM Role permissions are created before and deleted after EKS Cluster handling.
  # Otherwise, EKS will not be able to properly delete EKS managed EC2 infrastructure such as Security Groups.
  depends_on = [
    aws_iam_role_policy_attachment.igti-edc-AmazonEKSClusterPolicy,
    aws_iam_role_policy_attachment.igti-edc-AmazonEKSVPCResourceController,
  ]
}

output "endpoint" {
  value = aws_eks_cluster.k8s-igti-edc-desafiofinal.endpoint
}

output "kubeconfig-certificate-authority-data" {
  value = aws_eks_cluster.k8s-igti-edc-desafiofinal.certificate_authority[0].data
}