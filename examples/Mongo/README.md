##NHl1

全民健康保險保險費負擔金額表(三)
```
##DB
connection=MongoClient("mongodb://localhost:27017")
db=connection.nhi
nhidata=db.nhidata
```
* 'level':投保金額等級
* 'insurance':月投保金額
* 'family':被保險人眷屬數（僅本人為0）
* 'pay_p':被保險人負擔額
* 'pay_cpn':投保單位負擔金額
* 'pay_gov':政府負擔

##NHl2

勞 工 保 險 普 通 事 故 保 險 費 及 就 業 保 險 保 險 費 合 計 之 被 保 險 人 與 投 保 單 位 分 擔 金 額 表 (自104年1月1日起適用)

```
##DB
connection=MongoClient("mongodb://localhost:27017")
db=connection.nhi
nhidata=db.nhidata2
```
* 'day':投保日數
* 'payroll': 投保薪資
* 'Labor':勞工負擔
* 'Company':單位負擔
* 'Total':勞工加單位總額 
