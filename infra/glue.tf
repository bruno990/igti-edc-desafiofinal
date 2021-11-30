resource "aws_glue_catalog_database" "aws_glue_catalog_database" {
  name = "igti-edc-censo"
}

resource "aws_glue_crawler" "igti-edc-censo" {
  database_name = aws_glue_catalog_database.aws_glue_catalog_database.name
  name          = "glue-igti-edc-censo"
  role          = aws_iam_role.glue_role.arn

  s3_target {
    path = "s3://igti-edc-desafiofinal"
  }
}