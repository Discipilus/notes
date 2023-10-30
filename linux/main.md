# Linux

### Bash commands
```bash
sudo -s                  # gives you a shell like su
sudo -Hu root bash       # became a root
sudo -H -u edxapp bash   # change user

sudo chown -R edxapp xblock-in-video-quiz        # Change file owner and group
sudo chgrp -R edxapp xblock-in-video-quiz        # Change group ownership

### Services status
sudo service --status-all

### scp
scp root@app.dev.oc.big3.ru:dump_06-07-2022_16_00_30.sql.tar.gz /home/ad/Downloads/
scp root@app.test.oc.big3.ru:dump_06-07-2022_16_00_30.sql.tar.gz /home/ad/Downloads/

### HEX
xxd - make a hexdump or do the reverse.

### bin file to txt dump
xxd -p <bin_file> <fild_dump.txt>

### from txt dump to bin file
xxd -r -p <fild_dump.txt> <bin_file>

## history
history

1 ls -l
2 pwd
3 rm file.txt
> !2

### DNS lookup utility
dig -t A google.com
dig -t AAAA google.com

### find files more than 1G
sudo du -ah -t 1G /

### see what ports are in USE
less /etc/services

### Last bash command return value
echo $?

### ps
# with tree
ps -ejHf

### Listening ports
lsof -i :5432

# Check version of library
apt-cache policy libproj-dev

## Generate random strings
openssl rand -hex 32
df9ce0423c52a4aebe12fce49e1ba8b4371fa2c004e7cb467a7d016b05ae9957

### Remove empty directories
find . -depth -empty -type d -delete

### Start utility with envs
env B3_IS_LOCAL=111 TTT=333 ./manage.py runserver 0.0.0.0:8000


### Inet domain address check
nslookup <domain_name>

### find and grep actions
grep "EXPRESSION" `find . -name "*.po"`
find . -name "*.po" -exec grep -H "EXPRESSION" {} \;
find conf/locale/ -name "*.po" -exec bash -c "grep -H 'Daimler. All Rights Reserved.' {} | grep -v '2020'" \;
find . -name "*.py" -exec bash -c "grep -A 1 '@transition' {} | grep -v DocStatusTransition | grep -v '@transition' " \;
sudo find /edx/var/log/ -type f -exec bash -c 'grep -i -H "Skip the following calculation for User\|Updating aggregators in" {} | tail -n 2' \;
# Just files names
find . -type f -exec grep -l "The EPAM Continuum Podcast Network" {} \;

### loop cyclic grep
tail -f test_results.txt | grep 'FAILED'

### Disc formatting
sudo gdisk /dev/sdg1
sudo sgdisk -e /dev/sdh1


### One line bash loop:
# Repos git reset, git checkout, git clean -fd
REPOS=`ls`; curr_dir=`pwd`; for repo in $REPOS ; do echo $repo; cd $repo; git reset HEAD; git checkout -- '*'; git clean -fd; git status; cd ..; cd $curr_dir;  done

# Git checkout new_branch
REPOS=`ls`; curr_dir=`pwd`; for repo in $REPOS ; do echo $repo; cd $repo; git fetch origin; git checkout origin/master_dloc; git branch -v; cd ..; cd $curr_dir;  done

# Repos git log
REPOS=`ls`; curr_dir=`pwd`; for repo in $REPOS ; do echo $repo; cd $repo; git log -2 --pretty=oneline --graph; cd ..; cd $curr_dir;  done

# Repos git status
REPOS=`ls`; curr_dir=`pwd`; for repo in $REPOS ; do echo $repo; cd $repo; git status; cd ..; cd $curr_dir;  done

# Create empty files and Add 'Test Content' to all files in directory
ls ~/Projects/big3/app-back/rpn/services/tests/fixtures/multiple_project_attachements/SignedContent/ | xargs touch
FILES=`ls`; curr_dir=`pwd`; for file in $FILES ; do echo $file; echo "Test Content" > $file;  done

### Some other
REPOS=`ls`; curr_dir=`pwd`; for repo in $REPOS ; do echo $repo; cd $repo; git status; cd ..; cd $curr_dir;  done

REPOS=`ls`; curr_dir=`pwd`; for repo in $REPOS ; do echo $repo; cd $repo; git reset HEAD; git checkout -- '*'; git clean -fd; git fetch origin; git checkout qa_100; git branch -v; cd ..; cd $curr_dir;  done
```

### Archives
#### zip
```bash
zip -r conf.zip conf
```

#### unzip
```bash
unzip -o conf.zip -d conf
```

#### tar-gzip
```bash
# make archive of course directory
tar -zcvf course.tar.gz course

# Extract from archive
tar -xvzf GDAL-3.5.0.3.tar.gz
```

### linux hotkeys in command line
```
ctrl+a   - to beginning of line
ctrl+e   - to end of line
ctrl+w   - remove the latest word in command line
ctrl+l   - screen clear
```

#### curl
```bash
curl "https://app.dev.oc.big3.ru/api/wf__contract__contract_takeout/operation/signatures_for_print_forms/?query=^%^7Bid,name,datetime_create,is_outdated,pdf^%^7Bfile^%^7D,pdf_for_print^%^7Bfile^%^7D,docx^%^7Bfile^%^7D,author^%^7Bname^%^7D,template^%^7Bid^%^7D^%^7D&account_exists=y" ^
  -H "authority: app.dev.oc.big3.ru" ^
  -H "accept: application/json, text/plain, */*" ^
  -H "accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7" ^
  -H "authorization: Bearer d734d0e52e8648429a06e4ca906bbc81" ^
  -H "content-type: application/json" ^
  -H "origin: http://localhost:4200" ^
  -H "referer: http://localhost:4200/" ^
  -H "sec-ch-ua: ^\^"Not?A_Brand^\^";v=^\^"8^\^", ^\^"Chromium^\^";v=^\^"108^\^", ^\^"Google Chrome^\^";v=^\^"108^\^"" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
  -H "sec-fetch-dest: empty" ^
  -H "sec-fetch-mode: cors" ^
  -H "sec-fetch-site: cross-site" ^
  -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36" ^
  --data-raw "^{^\^"signatures^\^":^[^{^\^"signatory^\^":5,^\^"sign^\^":^\^"MIIGhgYJKoZIhvcNAQcCoIIGdzCCBnMCAQExDjAMBggqhQMHAQECAgUAMAsGCSqGSIb3DQEHAaCC^\^\r^\^\nA+QwggPgMIIDj6ADAgECAhMSAGDixvCMbnDSm+mLAAEAYOLGMAgGBiqFAwICAzB/MSMwIQYJKoZI^\^\r^\^\nhvcNAQkBFhRzdXBwb3J0QGNyeXB0b3Byby5ydTELMAkGA1UEBhMCUlUxDzANBgNVBAcTBk1vc2Nv^\^\r^\^\ndzEXMBUGA1UEChMOQ1JZUFRPLVBSTyBMTEMxITAfBgNVBAMTGENSWVBUTy1QUk8gVGVzdCBDZW50^\^\r^\^\nZXIgMjAeFw0yMjEyMjkwOTI1MTZaFw0yMzAzMjkwOTM1MTZaMIHlMSQwIgYJKoZIhvcNAQkBFhVk^\^\r^\^\ncm96aHpoaW4ubi5lQG1haWwucnUxEzARBgNVBAMMCtCh0LDRiNCwIDIxLDAqBgNVBAsMI9Ch0LLQ^\^\r^\^\nvtC1INC/0L7QtNGA0LDQt9C00LXQu9C10L3QuNC1MSgwJgYDVQQKDB/QodCy0L7RjyDQvtGA0LPQ^\^\r^\^\nsNC90LjQt9Cw0YbQuNGPMRUwEwYDVQQHDAzQotCw0LzQsdC+0LIxLDAqBgNVBAgMI9Ci0LDQvNCx^\^\r^\^\n0L7QstGB0LrQsNGPINC+0LHQu9Cw0YHRgtGMMQswCQYDVQQGEwJSVTBmMB8GCCqFAwcBAQEBMBMG^\^\r^\^\nByqFAwICJAAGCCqFAwcBAQICA0MABEBEiLqP7g7bxXNTjYfZJ92jJqtB+TZh1PFQfsa6hlTaJD6O^\^\r^\^\nMdSZ8VXtIITpwDEqWFIwoXX3fZb7r3p3VCS9+ZOqo4IBdjCCAXIwDgYDVR0PAQH/BAQDAgTwMBMG^\^\r^\^\nA1UdJQQMMAoGCCsGAQUFBwMCMB0GA1UdDgQWBBSjmsN+GwACQHLc6NI2HwD7mIrD0jAfBgNVHSME^\^\r^\^\nGDAWgBROgz4Uae/sXXqVK18R/jcyFklVKzBcBgNVHR8EVTBTMFGgT6BNhktodHRwOi8vdGVzdGNh^\^\r^\^\nLmNyeXB0b3Byby5ydS9DZXJ0RW5yb2xsL0NSWVBUTy1QUk8lMjBUZXN0JTIwQ2VudGVyJTIwMigx^\^\r^\^\nKS5jcmwwgawGCCsGAQUFBwEBBIGfMIGcMGQGCCsGAQUFBzAChlhodHRwOi8vdGVzdGNhLmNyeXB0^\^\r^\^\nb3Byby5ydS9DZXJ0RW5yb2xsL3Rlc3QtY2EtMjAxNF9DUllQVE8tUFJPJTIwVGVzdCUyMENlbnRl^\^\r^\^\nciUyMDIoMSkuY3J0MDQGCCsGAQUFBzABhihodHRwOi8vdGVzdGNhLmNyeXB0b3Byby5ydS9vY3Nw^\^\r^\^\nL29jc3Auc3JmMAgGBiqFAwICAwNBADvblk+e9JrcCneCbTLQVFwByMbr3uy5CLq1Vi3m9kVUHzoG^\^\r^\^\nkylT9uVgDhtaa0vLVKRbfrlp94Q5dxxeXWe9BhMxggJnMIICYwIBATCBljB/MSMwIQYJKoZIhvcN^\^\r^\^\nAQkBFhRzdXBwb3J0QGNyeXB0b3Byby5ydTELMAkGA1UEBhMCUlUxDzANBgNVBAcTBk1vc2NvdzEX^\^\r^\^\nMBUGA1UEChMOQ1JZUFRPLVBSTyBMTEMxITAfBgNVBAMTGENSWVBUTy1QUk8gVGVzdCBDZW50ZXIg^\^\r^\^\nMgITEgBg4sbwjG5w0pvpiwABAGDixjAMBggqhQMHAQECAgUAoIIBUjAYBgkqhkiG9w0BCQMxCwYJ^\^\r^\^\nKoZIhvcNAQcBMBwGCSqGSIb3DQEJBTEPFw0yMzAxMTMxMjQzMjdaMC8GCSqGSIb3DQEJBDEiBCBR^\^\r^\^\nrExuirDnmpiPij90xjJy4flfmLF1gdBDwIyILU0QijCB5gYLKoZIhvcNAQkQAi8xgdYwgdMwgdAw^\^\r^\^\ngc0wCgYIKoUDBwEBAgIEIOjYAa/r83dm1KBR//bO5oUa+ev0eOXWM73HqpyQpB9nMIGcMIGEpIGB^\^\r^\^\nMH8xIzAhBgkqhkiG9w0BCQEWFHN1cHBvcnRAY3J5cHRvcHJvLnJ1MQswCQYDVQQGEwJSVTEPMA0G^\^\r^\^\nA1UEBxMGTW9zY293MRcwFQYDVQQKEw5DUllQVE8tUFJPIExMQzEhMB8GA1UEAxMYQ1JZUFRPLVBS^\^\r^\^\nTyBUZXN0IENlbnRlciAyAhMSAGDixvCMbnDSm+mLAAEAYOLGMB8GCCqFAwcBAQEBMBMGByqFAwIC^\^\r^\^\nJAAGCCqFAwcBAQICBEDuEc/3xUY/HFN96Iz70M1KQNeNNQeYvcvyO8/ycmwp52tEvXtK16+VwcJj^\^\r^\^\nti2u9ix8g7aVHGqpNm1Vuf9u1gCt^\^",^\^"doc_template_scan^\^":1152^},^{^\^"signatory^\^":5,^\^"sign^\^":^\^"MIIGhgYJKoZIhvcNAQcCoIIGdzCCBnMCAQExDjAMBggqhQMHAQECAgUAMAsGCSqGSIb3DQEHAaCC^\^\r^\^\nA+QwggPgMIIDj6ADAgECAhMSAGDixvCMbnDSm+mLAAEAYOLGMAgGBiqFAwICAzB/MSMwIQYJKoZI^\^\r^\^\nhvcNAQkBFhRzdXBwb3J0QGNyeXB0b3Byby5ydTELMAkGA1UEBhMCUlUxDzANBgNVBAcTBk1vc2Nv^\^\r^\^\ndzEXMBUGA1UEChMOQ1JZUFRPLVBSTyBMTEMxITAfBgNVBAMTGENSWVBUTy1QUk8gVGVzdCBDZW50^\^\r^\^\nZXIgMjAeFw0yMjE
```
```shell
curl --location --request POST 'https://gronvos.ru/api/storage/upload/' --header 'Authorization: Bearer a159073fddbe4e02a116ecebb2379b61' --header 'Cookie: multidb_pin_writes=y' --form 'file=@"/home/ad/Pictures/test_images/background.jpg"'
```

#### kill
```shell
- SIGTERM (15): Terminate process gracefully
- SIGINT (2): Interrupt process from the keyboard (e.g. Ctrl-C)
- SIGHUP (1): Hangup detected on controlling terminal or death of controlling process
- SIGKILL (9): Kill process immediately and forcefully
- SIGSTOP (19): Stop a process
- SIGCONT (18): Continue a stopped process
- SIGQUIT (3): Quit process and generate core dump
```

