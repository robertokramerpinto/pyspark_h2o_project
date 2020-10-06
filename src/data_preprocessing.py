from src.etl import etl

if __name__ == '__main__':

    data = etl.create_sample_dataset()
    print("Sample data created")
    print(data.shape)