import os
import glob
import boto
import boto.s3.connection
import pronouncing

def jesterClue():
    dirname = os.getcwd()

    f = open(f"{dirname}/linodeCreds.txt")
    access_key = f.readline()
    secret_key = f.readline()
    f.close()

    access_key = access_key.strip()
    secret_key = secret_key.strip()

    conn = boto.connect_s3(
            aws_access_key_id = access_key,
            aws_secret_access_key = secret_key,
            host = 'us-east-1.linodeobjects.com',
            #is_secure=False,               # uncomment if you are not using ssl
            calling_format = boto.s3.connection.OrdinaryCallingFormat(),
            )

    for bucket in conn.get_all_buckets():

        name = bucket.name,
        created = bucket.creation_date,
        print (f"{name}\t{created}")

    for key in bucket.list():
        #print(key.get_acl())
        name = key.name,
        size = key.size,
        modified = key.last_modified,
        print (f"{name}\t{size}\t{modified}")
        try:
            if not os.path.isfile(f'{dirname}/scavenger-bucket/{name[0]}'):
                try:
                    #create folder
                    if "/" in name[0]:
                        folderPath = name[0].split('/')
                        print("folderPath: ")
                        print(folderPath[0])
                        os.makedirs(f'{dirname}/scavenger-bucket/{folderPath[0]}')
                        #then add file
                        key.get_contents_to_filename(f'{dirname}/scavenger-bucket/{folderPath[0]}{folderPath[1]}')
                    else:
                        key.get_contents_to_filename(f'{dirname}/scavenger-bucket/{name[0]}')
                except:
                    pass
        except:
            pass


    #get most recent file
    list_of_files = glob.glob(f'{dirname}/scavenger-bucket/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    #print (latest_file)

    j = open(latest_file)
    jesterCommand = j.readline()
    j.close()

    print(latest_file)
    print(jesterCommand)
    rhymes = pronouncing.rhymes(jesterCommand)

    print(rhymes)
    #get first rhyme
    if not rhymes:
        rhymes = "no clue found."
    else:
        rhymes = "Jester sound rhymes with "+rhymes[0]

    return rhymes