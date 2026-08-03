# Architecture RFC

## Introduction
The Dexma Framework is designed to operate in a decentralized environment, where agents can communicate and coordinate with each other directly.

## Architecture
The framework consists of the following components:
* **Agent**: The basic building block of the framework, responsible for making decisions and taking actions.
* **Registry**: A centralized registry for agents to register and discover each other.
* **Service**: A provider of functionality that can be requested by agents.
* **Storage**: A centralized storage system for data.
* **Analytics**: A component responsible for generating insights from data.

## Decision
The proposed architecture has been decided based on the following factors:
* **Scalability**: The framework must be able to scale horizontally, allowing for the addition of new agents and services as needed.
* **Flexibility**: The framework must provide a flexible foundation for building a wide range of decentralized applications.
* **Autonomy**: The framework must enable agents to make decisions and adapt to changing environments.