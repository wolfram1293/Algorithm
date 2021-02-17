import sys
import urllib3

def main(argv):
    for i, v in enumerate(argv):
        q="{1}".format(i, v)
    url = 'http://challenge-server.code-check.io/api/hash'
    http = urllib3.PoolManager()
    response = http.request('GET',url,fields={'out': 'json','q':q})
    a=response.data.decode('utf-8').split(":")
    ans=a[len(a)-1].replace('"', '')
    ans=ans.replace('}', '')
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])