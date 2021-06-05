  def last200lines(file):
    with open(file) as f:
        for line in (f.readlines() [-200:]):
            print(line, end ='')
  
  
if __name__ == '__main__':
    file = 'cron.log'
    try:
        last200lines(file)
    except:
        print('not found')
