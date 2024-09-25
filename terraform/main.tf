provider "google" {
  project = "concrete-detection-5"
  region  = "us-central1"
}

resource "google_container_cluster" "leyline-cluster" {
  name     = "leyline-cluster"
  location = "us-central1-a"  # Replace with your desired zone
  initial_node_count = 2

  # Use the default VPC and subnet settings
  network            = "default"
  subnetwork         = "default"

  # Enable the GKE Autopilot mode
  release_channel {
    channel = "REGULAR"
  }
}

data "google_container_cluster" "leyline-cluster" {
  name     = google_container_cluster.leyline-cluster.name
  location = google_container_cluster.leyline-cluster.location
}

output "cluster_name" {
  value = google_container_cluster.leyline-cluster.name
}
