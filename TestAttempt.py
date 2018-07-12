import tablib
from import_export import resources
from inventoryManagement.modelsList.recordModel import record
record_resource = resources.modelresource_factory(model=record)()
dataset = tablib.Dataset(['','admin','A-IT-DES-0362','SMC-I.T-DEC-111','Desktop','DELL OPTIPLEX 9020','H9KHG A01','DELL','9020','C4LH622','IT','ADMIN','1ST','OPEN AREA','Check Asset 5000000336,2018'], headers=['id','name','deviceTag','old_device_tag','device','item_description','serial_no','brand','model_no','service_tag','department','building','floor','room','remarks','year'])
result = record_resource.import_data(dataset, dry_run=True)
print(result.has_errors())
result = record_resource.import_data(dataset, dry_run=False)