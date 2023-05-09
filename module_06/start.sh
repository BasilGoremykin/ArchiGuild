echo "without cache"
wrk -d 60 -t 50 -c 50 --latency -s ./get.lua http://localhost:8081/

echo "with cache"
wrk -d 60 -t 50 -c 50 --latency -s ./get.lua http://localhost:8082/