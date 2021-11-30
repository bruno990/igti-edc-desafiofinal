resource "aws_iam_role" "glue_role" {
    name = "glue_role"

    assume_role_policy = jsonencode({
        Version = "2012-10-17"
        Statement = {
            Action = "sts:AssumeRole"
            Effect = "Allow"
            Sid = ""
            Principal = {
                Service = "glue.amazonaws.com"
            }
        }
    })
  
}