---
id: f44fs6lybpwzuc3oyhhzxkx
title: k8s使用教程
desc: ''
updated: 1682775101729
created: 1682763358880
---




## 简介

Kubernetes（通常简称为"k8s"）是一个开源的容器编排和管理平台，由Google公司开发并捐赠给Cloud Native Computing Foundation（CNCF）管理。

Kubernetes旨在帮助用户更轻松地部署、扩展和管理应用程序，以及提高应用程序的可靠性和可伸缩性。它支持多种容器运行时，如Docker、CRI-O等，并提供了丰富的API和工具，以便用户更轻松地管理容器、应用程序和相关资源。

Kubernetes采用了微服务架构的思想，通过将应用程序拆分成多个小型、独立的服务，并将它们部署到容器中，来提高应用程序的可靠性和可维护性。同时，Kubernetes还提供了丰富的服务发现、负载均衡、容错和自动扩展等功能，以便用户更轻松地管理应用程序。

总之，Kubernetes是一个用于容器编排和管理的开源平台，旨在提高应用程序的可靠性和可伸缩性，支持多种容器运行时，并提供了丰富的API和工具，以便用户更轻松地管理容器、应用程序和相关资源。

## 教程

### 架构

> 参考: https://devopscube.com/kubernetes-architecture-explained/

![](https://minio.kevin2li.top/image-bed/202304291822110.png)

#### Control Plane Components 
* `kube-apiserver`

在Kubernetes中，API Server是一个核心组件，它提供了Kubernetes API的前端，是Kubernetes集群中所有资源的唯一访问点。API Server充当了所有操作的统一网关，接收来自kubectl等客户端工具和其它Kubernetes组件的请求，然后根据请求的内容，向etcd存储库读取或更新状态，最后返回响应。

API Server为Kubernetes系统提供了一种强大的方式来控制、管理和监视各种资源和对象，例如Pod、Service、Deployment、ConfigMap、Secret等等。它还允许开发者通过自定义资源定义（Custom Resource Definitions）来扩展Kubernetes API，以支持特定于应用程序或行业的自定义资源类型。除此之外，API Server还提供了认证和授权机制，用于保护Kubernetes集群的安全。

* `etcd`

在Kubernetes中，`etcd`是用于存储集群状态的分布式键值存储系统。它是一个高可用的、强一致性的、分布式系统，通常运行在Kubernetes集群的控制平面节点上。etcd存储着Kubernetes集群的配置数据、状态信息和元数据，包括了节点、服务、副本集、部署、配置文件等。etcd使用Raft算法来保证数据的一致性和可靠性，确保Kubernetes集群的高可用和稳定性。在Kubernetes中，API Server是与etcd进行交互的唯一组件。

* `kube-scheduler`

在Kubernetes中，`Scheduler`是一个核心组件，它负责将新的Pod分配给可用的工作节点（Node）。当一个新的Pod被创建时，它会根据Pod的调度需求，如资源限制、亲和性、反亲和性等，选择一个最适合的节点进行调度。

`Scheduler`通常运行在Kubernetes集群的控制平面节点上，它通过与API Server交互来了解当前的集群状态和Pod的调度需求，并将未调度的Pod与可用的节点进行匹配，从而完成Pod的调度过程。`Scheduler`是一个可插拔的组件，可以根据实际需求定制和扩展调度算法。同时，Kubernetes还提供了调度器调度策略和插件的配置，以满足不同的调度需求。

* `kube-controller-manager`

![](https://minio.kevin2li.top/image-bed/202304291911696.png)

在Kubernetes中，`Controller Manager`是一个核心组件，它负责管理集群中的控制器（Controller）。控制器是一类负责维护Kubernetes系统中期望状态和实际状态一致的核心组件，例如Replication Controller、Deployment、StatefulSet、DaemonSet等等。

`Controller Manager`通常运行在Kubernetes集群的控制平面节点上，它通过与API Server交互来了解当前的集群状态，并根据期望状态与实际状态之间的差异，执行相应的操作，以确保集群的状态始终与期望状态一致。例如，当一个Pod被终止时，Replication Controller会创建一个新的Pod来替换它，以保持Pod的副本数量与期望值相同。

`Controller Manager`是一个可插拔的组件，可以根据实际需求定制和扩展不同类型的控制器。同时，Kubernetes还提供了控制器的配置和管理方式，以满足不同的需求和场景。

* `cloud-controller-manager`


在Kubernetes中，`Cloud Controller Manager`是一个可选组件，它负责管理与云平台相关的资源，例如负载均衡器、云盘、云存储等等。

`Cloud Controller Manager`运行在Kubernetes集群的控制平面节点上，通过与云平台API交互来管理这些资源。它与Kubernetes API Server交互，接收Kubernetes系统中的资源请求，并将这些请求翻译成云平台API调用。例如，在AWS云平台上，`Cloud Controller Manager`可以创建和管理Elastic Load Balancer，将Kubernetes Service暴露为外部负载均衡器。在GCP上，`Cloud Controller Manager`可以管理Persistent Disk资源，为Pod提供持久化存储。

`Cloud Controller Manager`是一个可插拔的组件，可以根据实际需求选择和配置不同类型的云平台资源。同时，Kubernetes还提供了云平台提供商相关的插件和配置选项，以方便云原生应用程序在不同云平台上的部署和管理。

#### Worker Node Components

* `kubelet` 

![](https://minio.kevin2li.top/image-bed/202304291912171.png)

在Kubernetes中，`kubelet`是一个核心组件，它运行在每个节点上，负责管理节点上的容器和镜像。

`kubelet`与Kubernetes API Server交互，获取当前节点上需要运行的Pod的信息，并根据这些信息创建、启动和停止相应的容器。同时，`kubelet`还负责监控这些容器的状态，并将容器的状态信息上报给Kubernetes API Server。

`kubelet`还负责管理节点上的容器和镜像，包括拉取、删除和清理过期的镜像，以确保节点上的存储空间得到充分利用。

除了与Kubernetes API Server交互外，`kubelet`还通过容器运行时接口（如Docker、CRI-O、containerd等）与容器运行时进行通信，管理容器的生命周期，并监视容器的资源使用情况。

总之，`kubelet`是Kubernetes集群中非常重要的一个组件，它负责将Kubernetes集群中的抽象概念（如Pod、容器）转化为在节点上运行的实际进程，是Kubernetes集群中实现容器编排和管理的关键组件之一。

* `kube-proxy`

在Kubernetes中，`kube-proxy`是一个核心组件，它运行在每个节点上，负责实现Kubernetes Service的网络代理和负载均衡功能。

`kube-proxy`通过监视Kubernetes API Server上的Service和Endpoint对象，了解哪些Service需要暴露到集群内部和外部，并且哪些后端Pod是Service的目标。然后，`kube-proxy`通过在节点上配置iptables规则或者ipvs规则（如果使用ipvs模式）来实现服务的负载均衡和代理。

当Service的Cluster IP被请求时，`kube-proxy`会使用相应的负载均衡算法选择一个后端Pod，并将请求转发给该Pod，从而实现服务的访问。此外，`kube-proxy`还可以支持通过NodePort和LoadBalancer等方式将Service暴露到集群外部，并实现相应的网络代理和负载均衡功能。

总之，`kube-proxy`是Kubernetes集群中非常重要的一个组件，它负责实现Kubernetes Service的网络代理和负载均衡功能，是Kubernetes集群中实现服务发现和负载均衡的关键组件之一。

* `Container runtime`

在Kubernetes中，Container runtime是指运行容器的软件。Kubernetes支持多种容器运行时，如Docker、CRI-O、containerd等。

容器运行时负责管理容器的生命周期，包括创建、启动、停止和销毁容器。容器运行时还负责管理容器的文件系统、网络和进程等资源，并确保容器能够在隔离的环境中运行。

在Kubernetes中，kubelet通过与容器运行时的接口（如Docker API、CRI-O API等）进行通信，与容器运行时交互，管理容器的生命周期，并监视容器的资源使用情况。

总之，容器运行时是Kubernetes集群中非常重要的一个组件，它负责管理容器的生命周期，并确保容器能够在隔离的环境中运行，是Kubernetes集群中实现容器编排和管理的关键组件之一。

### 术语
xx

### `kubectl`常用命令

`kubectl`是Kubernetes的命令行工具，可以用于管理Kubernetes集群、部署应用程序、监视集群状态等操作。下面是`kubectl`的一些基本用法：

``` bash
# 查看kubectl版本
kubectl version

# 查看配置
kubectl config view

# 查看集群信息
kubectl cluster-info

# 查看节点信息
kubectl get nodes

# 查看命名空间信息
kubectl get namespaces

# 创建一个deployment
kubectl create deployment <deployment-name> --image=<image-name>

# 查看deployment信息
kubectl get deployments

# 查看service信息
kubectl get services

# 端口转发到本地
kubectl port-forward <pod-name> <local-port>:<pod-port>

# 查看pod日志
kubectl logs <pod-name>

# 查看pod信息
kubectl get pods

# 进入一个pod
kubectl exec -it <pod-name> bash

# 删除pod
kubectl delete pod <pod-name>
```
### 举例

#### 部署
``` yaml 
apiVersion: apps/v1	#与k8s集群版本有关，使用 kubectl api-versions 即可查看当前集群支持的版本
kind: Deployment	#该配置的类型，我们使用的是 Deployment
metadata:	        #译名为元数据，即 Deployment 的一些基本属性和信息
  name: nginx-deployment	#Deployment 的名称
  labels:	    #标签，可以灵活定位一个或多个资源，其中key和value均可自定义，可以定义多组，目前不需要理解
    app: nginx	#为该Deployment设置key为app，value为nginx的标签
spec:	        #这是关于该Deployment的描述，可以理解为你期待该Deployment在k8s中如何使用
  replicas: 1	#使用该Deployment创建一个应用程序实例
  selector:	    #标签选择器，与上面的标签共同作用，目前不需要理解
    matchLabels: #选择包含标签app:nginx的资源
      app: nginx
  template:	    #这是选择或创建的Pod的模板
    metadata:	#Pod的元数据
      labels:	#Pod的标签，上面的selector即选择包含标签app:nginx的Pod
        app: nginx
    spec:	    #期望Pod实现的功能（即在pod中部署）
      containers:	#生成container，与docker中的container是同一种
      - name: nginx	#container的名称
        image: nginx:1.7.9	#使用镜像nginx:1.7.9创建container，该container默认80端口可访问
```

``` bash 
# 启动
kubectl apply -f nginx-deployment.yaml

# 查看 Deployment
kubectl get deployments

# 查看 Pod
kubectl get pods
```

## 参考

1. https://devopscube.com/kubernetes-tutorials-beginners/
2. https://www.okteto.com/blog/kubernetes-basics/
3. https://kuboard.cn/