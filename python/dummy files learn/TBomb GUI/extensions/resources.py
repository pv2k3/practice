
def get_mail_info(target):
    mail_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
       
        if not re.search(mail_regex, target, re.IGNORECASE):
            msg = (False, 
                "The mail ({target})".format(target=target) + 
                " that you have entered is invalid")
            continue
        return msg + (target, )


from .utils.provider import APIProvider

def workernode(mode, cc_phone, n_sms, delay, max_threads):
    api = APIProvider(cc_phone[0], cc_phone[1], mode, delay=delay)
    # clr()
    print( f"""
    Gearing up the Bomber - Please be patient

    Please stay connected to the internet during bombing")
    
    API Version  : {api.api_version}
    Target       : {cc_phone[0] + cc_phone[1] }
    Amount       : {str(n_sms)}
    Threads      : {str(max_threads)} threads 
    Delay        : {str(delay)} seconds

    # This tool was made for fun and research purposes only.
    """)
    if len(APIProvider.api_providers) == 0:
        print("Your country/target is not supported yet")
        print("Feel free to reach out to us")
        sys.exit()

    success, failed = 0, 0
    from concurrent.futures import ThreadPoolExecutor, as_completed
    while success < n_sms:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = []
            for i in range(n_sms-success):
                jobs.append(executor.submit(api.hit))

            for job in as_completed(jobs):
                result = job.result()
                if result is None:
                    print( "Bombing limit for your target has been reached")
                    print("Try Again Later !!... exiting now")
                    sys.exit()
                if result:
                    success += 1
                else:
                    failed += 1
                # clr()
                print(f"Target: +{cc_phone[0]+cc_phone[1]}\n Success :{success}\n Failed :{failed} ")
    print("\n")
    return "Bombing completed!"
    sys.exit()






def selectnode(mode, cc_phone, n_sms, delay, n_threads):
    mode = mode.lower().strip()
    try:
       
        # check_intr()
        
        # notifyen()

        max_limit = {"sms": 500, "call": 15, "mail": 200}

        cc, target = "", ""

        if mode in ["sms", "call"]:
            cc, target = cc_phone
            if cc != "91":
                max_limit.update({"sms": 100})
        elif mode == "mail":
            target = get_mail_info(cc_phone[1])
        else:
            raise KeyboardInterrupt

        limit = max_limit[mode]
        while True:
            try:
                if n_sms > limit or n_sms == 0:
                    print("You have requested " + str(n_sms)
                                            + " {type}".format(
                                                type=mode.upper()))
                    print(
                        "Automatically capping the value"
                        " to {limit}".format(limit=limit))
                    n_sms = limit
                # delay = 0
                max_thread_limit = (n_sms//10) if (n_sms//10) > 0 else 1

                n_threads = n_threads if (
                    n_threads > 0) else max_thread_limit
                if (n_sms < 0 or delay < 0):
                    raise Exception
                break
            except KeyboardInterrupt as ki:
                raise ki
                break
            except Exception as e:
                print("Read Instructions Carefully !!!", e)
                break

        return workernode(mode, cc_phone,n_sms,delay,n_threads)
    except KeyboardInterrupt:
        print("Received INTR call - Exiting...")
        sys.exit()

