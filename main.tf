terraform {
  backend "s3" {
    bucket       = "manmohan-tf-state-7k2q9x"
    key          = "actions-playground/terraform.tfstate"
    region       = "eu-north-1"
    use_lockfile = true
    encrypt      = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "eu-north-1"
}

resource "aws_s3_bucket" "demo" {
  bucket = "my-demo-bucket-change-this-123"
}
