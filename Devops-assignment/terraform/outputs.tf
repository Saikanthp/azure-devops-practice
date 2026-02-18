output "alb_dns_name" {
  value       = aws_lb.main.dns_name
  description = "Public URL of the application load balancer"
}

output "redis_endpoint" {
  value = aws_elasticache_cluster.redis.cache_nodes[0].address
}