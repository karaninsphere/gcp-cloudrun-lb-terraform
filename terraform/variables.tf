variable "project_id" {
  description = "GCP Project ID"
}

variable "region" {
  description = "GCP region"
  default     = "asia-south1"
}

variable "service_name" {
  default = "cloudrun-sample-app"
}

variable "docker_repo" {
  default = "docker-repo"
}

variable "container_image" {
  description = "Cloud Run container image"
  type        = string
}