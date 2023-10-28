sshCli = ConnectHandler(**router)
    output = sshCli.send_command_timing('/system reboot')
    if 'Reboot, yes? [y/N]:' in output:
        output += sshCli.send_command_timing('y')
    print(output)


