# Use the official Ubuntu base image
FROM ubuntu:latest

# Set maintainer label
LABEL maintainer="msmr1986@gmail.com"

# Update the package manager and install essentials
RUN apt-get update && apt-get install -y \
    curl \
    coreutils \
    ca-certificates \
    nano \
    cron

# Cleanup package cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/* && service cron start

# Set the working directory (optional)
WORKDIR /home/myuser

# Set a non-root user (optional but recommended for security)
# RUN useradd -ms /bin/bash myuser
# USER myuser

# copy the script needed for lab from the host folder
COPY rx_poc.sh ./

# Create needed file for the lab
RUN touch rx_poc.log && touch historical_fc_accuracy.tsv && \
    header="year\tmonth\tday\thour\tobs_tmp\tfc_tmp" && \
    echo $header > rx_poc.log && \
    echo -e "year\tmonth\tday\tobs_tmp\tfc_temp\taccuracy\taccuracy_range" > historical_fc_accuracy.tsv

# make the script runnable
# RUN sudo chmod u+x /home/myuser/rx_poc.sh

# Example usage of the installed commands
CMD ["bash"]
