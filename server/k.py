from grobid_client.grobid_client import GrobidClient

client = GrobidClient(config_path="./config.json")
k = client.process("processFulltextDocument", "./uploads/hey.pdf")
print(k)