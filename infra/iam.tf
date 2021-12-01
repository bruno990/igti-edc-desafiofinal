resource "aws_iam_role" "glue_role" {
    name = "glue_role"

    assume_role_policy = jsonencode({
        "Version": "2012-10-17",
        "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::igti-edc-desafiofinal/*"
            ]
        }
    ]
    })
  
}