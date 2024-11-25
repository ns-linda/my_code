class NfsShareExpirationTime():
    def __init__(self):
        super(NfsShareExpirationTime, self).__init__()
        self.valid_nfs_versions = ["NFS_V4", "NFS_V3", "NFS_V34"]
        self.expiration_time =[0,5,30]
  
    def validate_share_info(self, share_info):

        for nfs_versions, expiration_time in share_info:
            if "".join(nfs_versions) not in self.valid_nfs_versions:
                print(f"Invalid NFS version in share_info: {nfs_versions}")
                return False

            if expiration_time not in self.expiration_time:
                print(f"Invalid expiration time in share_info: {expiration_time}")
                return False

            for expiration_time in self.expiration_time:
                # if expiration_time  in [exp_time for _, exp_time in share_info if "".join(nfs_versions) in _]:
                #     print(f"Invalid expiration time for NFS version {nfs_versions}: {expiration_time}")
                #     # return False
                e=[]
                for _, exp_time in share_info:
                    if "".join(nfs_versions) in _:
                        e.append(exp_time)
                                         


        return True
    def run(self):
        all_share_info = [(['NFS_V4'], 0), (['NFS_V4'], 5), (['NFS_V4'], 30), 
                          (['NFS_V3'], 0), (['NFS_V3'], 5), (['NFS_V3'], 30), 
                            ]
        self.validate_share_info(all_share_info)

if __name__ == "__main__":
    obj = NfsShareExpirationTime()
    obj.run()
