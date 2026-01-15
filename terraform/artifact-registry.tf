resource "google_artifact_registry_repository" "docker_repo" {
  location      = var.region
  repository_id = var.docker_repo
  format        = "DOCKER"
}
