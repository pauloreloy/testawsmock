

from classes.AWS import AWS

if __name__ == "__main__":
    aws = AWS()
    cont = aws.get_s3_object("arquivosgerais", "bot.env")
    print(cont)