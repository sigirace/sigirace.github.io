

## EntryPoints

### 📒 Config_router.yaml

**EntryPoint**

```yaml
entryPoints:
  external:
    impl: http
    port: 6661
    version: v2
    properties:
      routePath: route
  ctl:
    impl: grpc
    port: 6651
    version: v1
    properties:
```



### 📒 router_factory.go

**buildEntryPoints**

```go
func buildEntryPoints(config *types.RouterServerConfig, loggerFactory logger.Factory, routerContext *types.RouterContext) {
	for name, epConf := range config.EntryPoints {
		ep := entrypoint2.NewEntryPoint(*epConf, loggerFactory)
		routerContext.EntryPoints.Put(name, ep)
		if routerContext.Trace != nil {
			ep.SetTrace(routerContext.Trace)
		}
		switch epConf.Impl {
		case entrypoint2.TypeHttp:
			initHttpEntryPoint(ep.(*entrypoint2.HttpServer), epConf, routerContext)
		case entrypoint2.TypeGrpc:
			initGrpcEntryPoint(ep.(*entrypoint2.GrpcServer), epConf, routerContext)
		default:
			panic("Unsupported EntryPoint type " + epConf.Impl)
		}
	}
}
```

| name     | epConf.Impl | epConf.Port | ep 타입 (캐스팅) |
| -------- | ----------- | ----------- | ---------------- |
| external | http        | 6661        | HttpServer       |
| ctl      | grpc        | 6651        | GrpcServer       |



### 📒 factory.go

**NewEntryPoint**

```go
func NewEntryPoint(config Config, loggerFactory logger.Factory) EntryPoint {
	logger := loggerFactory.GetLogger(fmt.Sprintf("%s_%s_server", config.Name(), config.Impl))

	switch config.Impl {
	case TypeHttp:
		return NewHttpServer(&config, logger)
	case TypeHttp2:
		return NewHttp2Server(&config, logger)
	case TypeQuic:
		return NewQuicServer(&config, logger)
	case TypeGrpc:
		return NewGrpcServer(&config, logger)
	default:
		panic("Unknown entrypoint type " + config.Impl)
	}
}
```



**NewHttpServer**

| 필드                 | 값                                            |
| -------------------- | --------------------------------------------- |
| `name`               | `{config.Name()}_{config.Impl}_{config.Port}` |
| `config`             | `config` 객체 그대로 참조                     |
| `ginEngine`          | `gin.Default()` (CORS 설정 포함)              |
| `logger`             | `logger` 객체 그대로 참조                     |
| `protocol`           | `TypeHttps` (TLS 설정 시) / `TypeHttp` (기본) |
| `secured`            | `true` (TLS 설정 시) / `false` (기본)         |
| `MaxMultipartMemory` | `50 MiB (50 << 20)`                           |



**initHttpEntryPoint**

- policy

```go
type InboundPolicyV1 struct {
	genReqId       GenReqID
	genSessId      GenSessID
	keySelector    KeySelector
	tenantProvider tenant.Provider
	context        *types.RouterContext
	logger         logger.Logger
}
```

