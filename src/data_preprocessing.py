from src.etl import create_sample_dataset

if __name__ == '__main__':

    data = create_sample_dataset()
    print("Sample data created")
    print(data.shape)